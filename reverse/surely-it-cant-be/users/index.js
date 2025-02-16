const { spawn } = require("child_process");

const processes = [];

function spawnProcess() {
    const delay = Math.random() * 50 + 50;
    setTimeout(() => {
        const process = spawn("node", ["agent.js"]);

        console.log(`Spawned process PID: ${process.pid}`);
        processes.push(process);

        process.stdout.on("data", (data) => {
            console.log(`Process ${process.pid} output: ${data}`);
        });

        process.stderr.on("data", (data) => {
            console.error(`Process ${process.pid} error: ${data}`);
        });

        process.on("exit", (code) => {
            console.log(`Process ${process.pid} exited with code ${code}`);
        });
    }, delay);
}

for (let i = 0; i < 10; i++) {
    spawnProcess();
}

function shutdown() {
    console.log("Shutting down all processes...");
    processes.forEach((child) => {
        console.log(`Killing process PID: ${child.pid}`);
        child.kill();
    });
    process.exit(0);
}

process.on("SIGINT", shutdown);
process.on("SIGTERM", shutdown);
