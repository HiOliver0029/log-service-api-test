const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;
const back_port = 5001

app.use(express.static('public'));
app.use(express.json());

app.get('/logs', async (req, res) => {
  try {
    const response = await axios.get(`http://localhost:${back_port}/logs`);
    res.json(response.data);
  } catch (error) {
    console.error('Error fetching logs from backend:', error);
    res.status(error.response.status).json(error.response.data);
  }
});

app.listen(port, () => {
  console.log(`Frontend app listening at http://localhost:${port}`);
});
