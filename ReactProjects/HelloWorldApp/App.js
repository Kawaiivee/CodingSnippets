import React, { Component } from 'react';
import { AppRegistry, Text, View, Image } from 'react-native';

class Greeting extends Component{
	render(){
		return (
		<Text>Hello {this.props.name}!</Text>
		);
	}
}

export default class HelloWorldApp extends Component {
  render() {
    let pic = {
    	uri: 'https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png'
    };
    return (
      <View style={{alignItems: 'center'}}>
        <Greeting name='To You' />
        <Greeting name='To Me' />
        <Greeting name='WORLD!!!!!' />
     	<Image source={pic} style={{width: 193, height: 110}}/>
      </View>
    );
  }
}

