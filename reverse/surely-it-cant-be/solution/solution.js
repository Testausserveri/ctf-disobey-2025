const fs = require("node:fs");
const crypto = require("node:crypto");

const parsed = fs.readFileSync("parsed.txt", "utf8").trim().split("\n");

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
    const decipher = crypto.createDecipheriv("aes-256-cbc", key, iv);
    return Buffer.concat([decipher.update(buf), decipher.final()]);
}

parsed.shift();
const encryptionKeyEntries = parsed.splice(0, 2);

let data = "";
for (const query of parsed) {
    const chunk = query.split(".").reverse().slice(6).reverse().join("");
    if (chunk === "fin") continue;
    data += chunk;
}

const encryptionKey = Buffer.from(
    encryptionKeyEntries.map(getFullIPv6).join("").replace(/:/g, ""),
    "hex"
);

const buf = parseBase36(data);
const decrypted = decrypt(buf, encryptionKey);
fs.writeFileSync("./trade-secrets.jpg", decrypted);
