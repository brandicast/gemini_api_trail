const { GoogleGenerativeAI } = require("@google/generative-ai");

// Access your API key as an environment variable (see "Set up your API key" above)
// Make sure to include these imports:
// import { GoogleGenerativeAI } from "@google/generative-ai";
const genAI = new GoogleGenerativeAI(process.env.API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });


console.log(model);

//result.then((result) => console.log(result.response.text), () => console.log("N/A"));

async function run() {
    const prompt = "Write a summary about thr startup Unlayer.";

    const result = await model.generateContentStream(prompt);

    let text = "";
    for await (const chunk of result.stream) {
        const chunkText = chunk.text();
        console.log(chunkText);
        text += chunkText;
    }

    // const result = await model.generateContent(prompt);
    // const response = result.response;
    // const text = response.text();
    // console.log(text);
}

run().catch((e) => {
    console.error("Something went wrong");
    console.log(e);
    process.exit(1);
});
