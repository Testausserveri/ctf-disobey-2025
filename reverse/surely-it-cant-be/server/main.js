const { Packet, createServer } = require("dns2");
const { randomBytes, createDecipheriv } = require("node:crypto");
const { mkdirSync, writeFileSync } = require("node:fs");

mkdirSync("./uploads", { recursive: true });

const sessions = new Map();
const inits = new Map();

function parseBase36(b36) {
    const base = BigInt(36);
    let result = BigInt(0);

    for (let i = 0; i < b36.length; i++) {
        const digitValue = BigInt(parseInt(b36[i], 36));
        result = result * base + digitValue;
    }

    const hexString = result.toString(16);
    const paddedHexString = hexString.length % 2 === 0 ? hexString : "0" + hexString;
    return Buffer.from(paddedHexString, "hex");
}

function decrypt(buf, key) {
    const iv = buf.subarray(0, 16);
    buf = buf.subarray(16);
    const decipher = createDecipheriv("aes-256-cbc", key, iv);
    return Buffer.concat([decipher.update(buf), decipher.final()]);
}

function toIPv6(buf) {
    // return [
    //     ...([...buf]
    //         .map((v) => v.toString(16).padStart(2, "0"))
    //         .join("")
    //         .match(/.{4}/g) ?? []),
    // ].join(":");
    return Object.values(Object.groupBy([...buf], (_, i) => Math.floor(i / 2)))
        .map(([a, b]) => (a * 256 + b).toString(16).padStart(4, "0"))
        .join(":");
}

function toIPv4(buf) {
    return [...buf].join(".");
}

function randomIPv6() {
    return toIPv6(randomBytes(16));
}

function randomIPv4() {
    return toIPv4(randomBytes(4));
}

const server = createServer({
    udp: true,
    tcp: true,
    handle: (request, respond) => {
        try {
            const response = Packet.createResponseFromRequest(request);
            const [question] = request.questions;
            if (
                request.questions.length !== 1 ||
                question.class !== Packet.CLASS.IN ||
                (question.type !== Packet.TYPE.A && question.type !== Packet.TYPE.AAAA) ||
                !question.name.endsWith(".s.tti.sh")
            ) {
                console.log("invalid query for", question.name);
                respond(response);
                return;
            }
            const [cmd, ...args] = question.name.split(".").reverse().slice(3);

            if (cmd === "b") {
                if (args.length !== 1) {
                    respond(response);
                    return;
                }
                const [initRandom] = args;
                if (question.type === Packet.TYPE.A) {
                    const sessionBytes = randomBytes(4);
                    const sessionAddress = toIPv4(sessionBytes);
                    const sessionKey = sessionBytes.reduce((a, c) => a * 256 + c, 0).toString(36);
                    console.log("new session request", initRandom);
                    inits.set(initRandom, sessionKey);
                    response.answers.push({
                        name: question.name,
                        type: Packet.TYPE.A,
                        class: Packet.CLASS.IN,
                        ttl: 5,
                        address: sessionAddress,
                    });
                    respond(response);
                    return;
                } else {
                    if (!inits.has(initRandom)) {
                        respond(response);
                        return;
                    }
                    const encryptionKey = randomBytes(32);
                    const sessionKey = inits.get(initRandom);
                    inits.delete(initRandom);
                    sessions.set(sessionKey, { encryptionKey, data: "" });
                    console.log("new session", sessionKey, encryptionKey);
                    const encryptionAddress1 = toIPv6(encryptionKey.subarray(0, 16));
                    const encryptionAddress2 = toIPv6(encryptionKey.subarray(16));
                    response.answers.push({
                        name: question.name,
                        type: Packet.TYPE.AAAA,
                        class: Packet.CLASS.IN,
                        ttl: 5,
                        address: encryptionAddress1,
                    });
                    response.answers.push({
                        name: question.name,
                        type: Packet.TYPE.AAAA,
                        class: Packet.CLASS.IN,
                        ttl: 5,
                        address: encryptionAddress2,
                    });
                    respond(response);
                    return;
                }
            }
            if (cmd === "d") {
                if (args.length < 2) {
                    respond(response);
                    return;
                }
                const [sessionKey, ...dataParts] = args;
                const data = dataParts.reverse().join("");
                if (!sessions.has(sessionKey)) {
                    respond(response);
                    return;
                }
                const session = sessions.get(sessionKey);

                if (data === "fin") {
                    const buf = parseBase36(session.data);
                    const decrypted = decrypt(buf, session.encryptionKey);
                    writeFileSync(`./uploads/${sessionKey}`, decrypted);
                    console.log("finished session", sessionKey);
                    sessions.delete(sessionKey);
                    response.answers.push({
                        name: question.name,
                        type: question.type,
                        class: Packet.CLASS.IN,
                        ttl: 5,
                        address: question.type === Packet.TYPE.A ? randomIPv4() : randomIPv6(),
                    });
                    respond(response);
                    return;
                }

                console.log("data for", sessionKey);
                session.data += data;

                response.answers.push({
                    name: question.name,
                    type: question.type,
                    class: Packet.CLASS.IN,
                    ttl: 5,
                    address: question.type === Packet.TYPE.A ? randomIPv4() : randomIPv6(),
                });
                respond(response);
                return;
            }
        } catch (e) {
            console.error(e);
        }
    },
});

server.on("listening", () => {
    console.log("Listening on", server.addresses());
});

server.listen({
    udp: {
        port: 53,
        address: "0.0.0.0",
    },
    tcp: {
        port: 53,
        address: "0.0.0.0",
    },
});
