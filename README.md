# AgentPay Wallet — sito tecnico pubblico

Sito informativo pubblico di **AgentPay Wallet**, progetto software di FSL Multiservice in sviluppo controllato.

**Live:** [agentpay.fslditta.com](https://agentpay.fslditta.com)

## Perimetro

La pagina documenta lo stato tecnico verificato del progetto. Non offre e non attiva wallet operativi, pagamenti, carte, conti, IBAN, credito, trasferimenti, trading, Open Banking o collegamenti a provider finanziari.

## Stato applicativo di riferimento

- Expo SDK 57.0.25
- React Native 0.86.3
- TypeScript
- 921 test passati e 8 saltati nell'ultima validazione registrata
- APK interna 1.1.0 completata
- candidato 1.1.1 pronto nel sorgente, in attesa di quota EAS e collaudo su dispositivo
- Open Banking e provider finanziari disattivati per policy (`enabled=false`, `networkRequestsAllowed=false`)
- Wallester rappresentato soltanto da dati mock read-only

Il codice dell'app mobile è disponibile nel repository [fslmultiservice22/agentpay-mobile-app](https://github.com/fslmultiservice22/agentpay-mobile-app).

## Pubblicazione

Il repository contiene un sito statico e una workflow GitHub Pages. Prima della pubblicazione, la validazione automatica deve confermare che metriche, toolchain e dichiarazioni finanziarie siano coerenti con il perimetro non transazionale.

© 2026 FSL Multiservice.
