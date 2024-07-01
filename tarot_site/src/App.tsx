import { useState, useEffect } from 'react';
import * as React from 'react';
import './App.css';
import CardList from './components/CardList';
import Card from './components/Card';




function App() {

  const [cardData, setCardData] = useState(null);

  const tempCard = {"Card Name":"The Fool","Major Arcana":true,"Reversed Meaning":"recklessness, taken advantage of, inconsideration","Upright Meaning":"innocence, new beginnings, free spirit"};

  // useEffect(() =>{
  //   fetch('http://127.0.0.1:5000/collect-data')
  //     .then(res => res.json())
  //     .then(resJson => setCardData(resJson['cards']))
  //     .catch(error => console.error(error));
  // }, []);

  return (
    <div>
      <Card name={tempCard['Card Name']} upright={tempCard['Upright Meaning']} reversed={tempCard['Reversed Meaning']} majorArcana={tempCard['Major Arcana']}/>
    </div>
  );
}

export default App;
