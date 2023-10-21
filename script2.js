
import OpenAIApi from 'openai';


const apiKey = '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'; // Replace with your actual API key

const openai = new OpenAIApi({ apiKey });

// Assuming you have a dataset of questions and answers
const dataset = [
  {
    question: "What is the history of the FDV?",
    answer: "The Flower Corso is the origin of the Harvest Festival. ... (rest of the answer)"
  },
  // Add more questions and answers as needed
];

async function getAnswer(question) {
  const messages = [
    {"role": "system", "content": "You are a helpful assistant."}, // System message to set the assistant's role
    {"role": "user", "content": question}, // User's question
  ];

  try {
    const response = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo', // Specify the chat model you want to use
      messages
    });

    const answer = response.choices[0].message.content;
    return answer;
  } catch (error) {
    console.error(error);
    return "Sorry, I couldn't understand your question.";
  }
}

// Example usage
const userQuestion = "What is the history of the FDV?";
getAnswer(userQuestion)
  .then(answer => console.log(answer))
  .catch(error => console.error(error));
