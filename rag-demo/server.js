// import express from "express";
// import cors from "cors";
// import bodyParser from "body-parser";
// import { chatting } from "./query.js";

// const app = express();
// app.use(cors());
// app.use(bodyParser.json());

// app.post("/chat", async (req, res) => {
//   try {
//     const { question } = req.body;
//     const answer = await chatting(question);
//     res.json({ answer });
//   } catch (err) {
//     console.error(err);
//     res.status(500).json({ error: "Something went wrong" });
//   }
// });

// app.listen(8000, () => console.log("🚀 Server running at http://localhost:8000"));
