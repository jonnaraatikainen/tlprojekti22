# Tietoliikenteen sovellusprojekti

## Kuvaus
Tietoliikennelabrassa on IoT-reititin (Raspberry Pi), joka on Oamkin kampusverkossa. Opiskelijoiden tehtävänä on koodata Arduinolle client, joka mittaa kiihtyvyysanturin 
dataa ja välittää tietoa langattomasti IoT-reitittimelle valmiiksi annetun speksin mukaisesti. IoT-reititin on asennettu valmiiksi ja varastoi vastaanotettua dataa 
MySQL-tietokantaan.

Tietokantaan tallentuvaan dataan on TCP-sokettirajapinta ja HTTP API. Kerättyä dataa haetaan rajanpinnasta omaan kannettavaan koodatulla ohjelmalla ja käsitellään 
koneoppimistarkoitukseen.

![image](https://user-images.githubusercontent.com/93710233/199669397-033d183c-42d3-48f6-b4f0-663541653774.png)
