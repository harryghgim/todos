import React, { Component } from 'react';
import axios from 'axios'; 

class App extends Component {
  state = {
    tasks: []
  }

  componentDidMount() {
    this.getTodos();
  }

  getTodos() {
    axios
      .get('http://localhost:8000/')
      .then(res => {
        this.setState({ tasks: res.data });
      })
      .catch(err => {
        console.log(err);
      })
  }

  render() {
    return (
      <div>
        {this.state.tasks.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <p>완료시각: {item.completed_at}</p>
          </div>
        ))}
      </div>
    )
  }
}

export default App;
