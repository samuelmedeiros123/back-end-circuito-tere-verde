const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

let parques = [
  { id: 1, nome: "PARNASO - Serra dos Orgaos" },
  { id: 2, nome: "Parque Montanhas de Teresopolis" },
  { id: 3, nome: "Parque Municipal" }
];

let trilhas = [
  { id: 1, parqueId: 1, nome: "Pedra do Sino", dificuldade: "dificil", tempo: "8h", status: "Aberta" },
  { id: 2, parqueId: 2, nome: "Cartao Postal", dificuldade: "media", tempo: "2h", status: "Aberta" },
  { id: 3, parqueId: 3, nome: "Pedra do Indaia", dificuldade: "facil", tempo: "1h", status: "Fechada" }
];

app.get('/', (req, res) => {
  res.json({ msg: "API Tere-Verde no ar!" });
});

app.get('/api/parques', (req, res) => {
  res.json(parques);
});

app.get('/api/trilhas', (req, res) => {
  res.json(trilhas);
});

app.listen(PORT, () => {
  console.log("Rodando em http://localhost:3000");
});
