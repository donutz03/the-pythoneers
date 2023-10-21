
import OpenAIApi from 'openai';


const apiKey = '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'; // Replace with your actual API key


const openai = new OpenAIApi({ apiKey });

const messages = [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Who won the world series in 2020?"},
  {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
  {"role": "user", "content": "Where was it played?"}
];

openai.chat.completions.create({
  model: 'gpt-3.5-turbo', // Specify the chat model you want to use
  messages
})
.then(response => {
    // console.log(response);
  console.log(response.choices[0].message.content);
})
.catch(error => console.error(error));


