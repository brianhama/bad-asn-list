#!/usr/bin/env node
const fs = require('fs');

const asns = [];
let asn_list = [];

const ASN_FILE = 'bad-asn-list.csv';
const ASN_JSON = 'bad-asn-list.json';
const NEW_ASN_FILE = 'bad-asn-list.csv.1';

const csvStringToArray = (strData) => {
  const objPattern = new RegExp(('(\\,|\\r?\\n|\\r|^)(?:"([^"]*(?:""[^"]*)*)"|([^\\,\\r\\n]*))'),'gi');
  let arrMatches = null;
  let arrData = [[]];
  // eslint-disable-next-line
  while (arrMatches = objPattern.exec(strData)) {
    if (arrMatches[1].length && arrMatches[1] !== ',') {
      arrData.push([]);
    }
    arrData[arrData.length - 1].push(arrMatches[2] ? 
      arrMatches[2].replace(new RegExp( '""', 'g' ), '"') :
      arrMatches[3]
    );
  }
  return arrData;
};

const importCsv = (csvString) => {
  const csvArray = csvStringToArray(csvString);
  // Remove csv header
  csvArray.shift();
  csvArray.forEach(a => {
    let asn = a[0];

    if (typeof asn === 'string') {
      asn = parseInt(asn.replaceAll('"', ''));
    }

    if (asn && !asns.includes(asn)) {
      asns.push(asn);
      asn_list.push({
        ASN: asn,
        Entity: a[1]
      });
    }
  });
};

const writeCsv = () => {
  fs.writeFileSync(ASN_JSON, JSON.stringify(asn_list, null, 2));
  fs.writeFileSync(ASN_FILE, 'ASN,Entity');
  asn_list.forEach(a => {
    fs.appendFileSync(ASN_FILE, `\n${a.ASN},"${a.Entity}"`);
  });
  console.log('Wrote new CSV');
};

const start = () => {
  const asn_original = fs.readFileSync(ASN_FILE, { encoding: 'utf8' });
  importCsv(asn_original);

  if (NEW_ASN_FILE && fs.existsSync(NEW_ASN_FILE)) {
    const asn_new = fs.readFileSync(NEW_ASN_FILE, { encoding: 'utf8' });
    importCsv(asn_new);
  }

  asn_list = asn_list.sort((a, b) => a.ASN - b.ASN);

  console.log(`Original CSV Length: ${csvStringToArray(asn_original).length - 1}`);
  console.log(`New CSV Length: ${asn_list.length}`);
  writeCsv();
};
start();
