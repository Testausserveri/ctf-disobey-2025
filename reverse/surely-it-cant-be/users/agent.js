const apis = ["cat", "dog", "joke", "trivia", "year", "advice", "programming-joke", "meme"];

async function main() {
    while (true) {
        const api = apis[Math.floor(Math.random() * apis.length)];
        const res = await fetch("http://localhost:8080/api/" + api);
        await res.arrayBuffer();
        await new Promise((res) => setTimeout(res, 100 + Math.random() * 200));
    }
}

main();
