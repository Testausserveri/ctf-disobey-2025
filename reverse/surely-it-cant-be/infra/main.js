const express = require("express");
const axios = require("axios");
const app = express();

app.get("/", async (req, res) => {
    res.send("Hello, World!");
});

app.get("/api/cat", async (req, res) => {
    try {
        const apiRes = await axios.get("https://api.thecatapi.com/v1/images/search");
        const imgRes = await axios.get(apiRes.data[0].url, { responseType: "arraybuffer" });
        res.header("content-type", imgRes.headers["content-type"]);
        res.send(imgRes.data);
    } catch (error) {
        console.error();
        res.status(500).json({ error: "Failed to fetch cat image" });
    }
});

app.get("/api/dog", async (req, res) => {
    try {
        const response = await axios.get("https://dog.ceo/api/breeds/image/random");
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: "Failed to fetch dog image" });
    }
});

app.get("/api/joke", async (req, res) => {
    try {
        const response = await axios.get("https://official-joke-api.appspot.com/random_joke");
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: "Failed to fetch joke" });
    }
});

app.get("/api/trivia", async (req, res) => {
    try {
        const response = await axios.get("http://numbersapi.com/random/trivia?json");
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: "Failed to fetch trivia" });
    }
});

app.get("/api/year", async (req, res) => {
    try {
        const response = await axios.get("http://numbersapi.com/random/year?json");
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: "Failed to fetch year fact" });
    }
});

app.get("/api/advice", async (req, res) => {
    try {
        const response = await axios.get("https://api.adviceslip.com/advice");
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: "Failed to fetch advice" });
    }
});

app.get("/api/programming-joke", async (req, res) => {
    try {
        const response = await axios.get("https://v2.jokeapi.dev/joke/Programming?type=single");
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: "Failed to fetch programming joke" });
    }
});

app.get("/api/meme", async (req, res) => {
    try {
        const response = await axios.get("https://meme-api.com/gimme");
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: "Failed to fetch meme" });
    }
});

app.listen(8080, () => {
    console.log("Server is running on port 8080");
});
