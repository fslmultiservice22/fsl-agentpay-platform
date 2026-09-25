import { readFileSync } from "node:fs";

const html = readFileSync(new URL("./index.html", import.meta.url), "utf8");
const readme = readFileSync(new URL("./README.md", import.meta.url), "utf8");
const corpus = `${html}\n${readme}`;

const required = [
  "921",
  "Expo SDK 57.0.25",
  "React Native 0.86.3",
  "Open Banking non attivo",
  "networkRequestsAllowed=false",
  "25 settembre 2026",
];

const forbidden = [
  "Expo SDK 54",
  "React Native 0.81",
  "Integrazione validata",
  "infrastruttura Open Banking integrata",
  "Payments: Stripe + Wise",
  "Swap & Trading (Uniswap",
];

for (const value of required) {
  if (!corpus.includes(value)) throw new Error(`Contenuto obbligatorio mancante: ${value}`);
}

for (const value of forbidden) {
  if (corpus.includes(value)) throw new Error(`Claim non consentito presente: ${value}`);
}

console.log("Contenuto AgentPay verificato: beta tecnica non transazionale.");
