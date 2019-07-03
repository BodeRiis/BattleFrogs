"use strict";

function GenerateBoard(props) {
    let water = [];
    let squareNames = []

    for (let row = 0; row < 10; row++) {
        let thisRow = []; 
            for (let col = 0; col < 10; col++) {

                thisRow.push(
                <i className="fas fa-water" key={row.toString().concat(col.toString())}></i>
            );
        }  
        water.push(<div className="game-row" key={'row'.concat(row.toString())}>{thisRow}</div>);
    }
    return <div className="board">{water}</div>;
}


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    userHits : 0,
    botHits : 0,
    };
}

    render () {
    return (

        <div>
        <h1>BattleFrogs JSX imported!</h1>
        <div>
            <GenerateBoard />
        </div>
        </div>

        );
    }

}


ReactDOM.render(
  <App />,
  document.getElementById('root')
);
