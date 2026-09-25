import { readFileSync } from "node:fs";

const html = readFileSync(new URL("./index.html", import.meta.url), "utf8");
const readme = readFileSync(new URL("./README.md", import.meta.url), "utf8");
const privacy = readFileSync(new URL("./privacy.html", import.meta.url), "utf8");
const terms = readFileSync(new URL("./terms.html", import.meta.url), "utf8");
const corpus = `${html}\n${readme}\n${privacy}\n${terms}`;

const required = [
  "921",
  "Expo SDK 57.0.25",
  "React Native 0.86.3",
  "Open Banking non attivo",
  "networkRequestsAllowed=false",
  "25 settembre 2026",
  "beta tecnica controllata e non transazionale",
  "non deve ricevere numeri di carta, IBAN",
];

const forbidden = [
  "Expo SDK 54",
  "React Native 0.81",
  "Integrazione validata",
  "infrastruttura Open Banking integrata",
  "Payments: Stripe + Wise",
  "Swap & Trading (Uniswap",
  "disponibile su App Store e Google Play",
  "Gestione locale di conti bancari e bonifici SEPA",
  "Portafoglio multi-chain per criptovalute",
  "dati finanziari locali",
];

for (const value of required) {
  if (!corpus.includes(value)) throw new Error(`Contenuto obbligatorio mancante: ${value}`);
}

for (const value of forbidden) {
  if (corpus.includes(value)) throw new Error(`Claim non consentito presente: ${value}`);
}

console.log("Contenuto AgentPay verificato: beta tecnica non transazionale.");
