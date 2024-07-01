import * as React from 'react';
import { useState, useEffect } from 'react';


interface CardProps {
    name: string,
    upright: string,
    reversed: string,
    majorArcana: boolean
}


function Card({name, upright, reversed, majorArcana} : CardProps){

    const [imgData, setImgData] = useState(null);
    const [imgName, setImgName] = useState(null);

    function trimName(){
        var nameArg = name.replace(/\s/g, "").toLowerCase();
        setImgName(trimName);
    }


    useEffect(() =>{
        var nameArg = name.replace(/\s/g, "").toLowerCase();
    fetch(`http://127.0.0.1:5000/get-card-img?img=${nameArg}.png`)
      .then(res => res.json())
      .then(resJson => setImgData(resJson['img']))
      .catch(error => console.error(error));
  }, []);


    return(
        <div>{name}, {upright}, {reversed}, {majorArcana}
            <img src={`data:image/png;base64,${imgData}`}/>   
        </div>
    );
}

export default Card;