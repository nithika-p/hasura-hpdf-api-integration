import React, { Component } from 'react';
import './App.css';
import robot from './robot.jpg';
import TextField from 'material-ui/TextField';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

class App extends Component {

  create(e) {
      e.preventDefault();
      let name = this.refs.myTextField.input.value;
      var xhr = new XMLHttpRequest();
      xhr.open("POST","https://app.depress64.hasura-app.io/", true);
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.send(JSON.stringify({
          "text": name
      }));
      xhr.onreadystatechange = function () {
        if (this.readyState != 4) return;

        if (this.status == 200) {
            var data = JSON.parse(this.responseText);
            document.getElementById("response").innerHTML = JSON.stringify(data)
        }
        // end of state change: it can be after some time (async)
    };

    }

 constructor(){
      super();
      this.create = this.create.bind(this);
    }
  render() {
    return (
      <div className="App">
      <MuiThemeProvider>
        <div className='text'>
          Say Something to Student helper bot
          Response format is {"[<entity_name>,<entity_value>]"}
        </div>
        <div className='main'>
          <form method="POST" action="/">
          <TextField  ref='myTextField' floatingLabelText="Enter some text" floatingLabelStyle={{fontSize:20}} />
          <button type="submit" name="button" value="client_msged" className='button' onClick={this.create}>Find intent</button>
          </form>
        </div>
        <div className='text'>
          RESPONSE :
        </div>
        <div className='response' id='response'>
        </div>
        </MuiThemeProvider>
      </div>
    );
  }
}

export default App;
