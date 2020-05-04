import 'package:flutter/material.dart';

class CustomRaisedButton extends StatelessWidget {
  CustomRaisedButton({this.text, this.onPressed});

  final String text;
  final Function onPressed;

  @override
  Widget build(BuildContext context) {
    return RaisedButton(
      elevation: 0.0,
      hoverElevation: 0.0,
      focusElevation: 0.0,
      highlightElevation: 0.0,
      color: Colors.black38.withOpacity(0.1),
      onPressed: onPressed,
      child: Text(
        text,
        style: TextStyle(
          fontSize: 15.0,
          color: Colors.black87,
          fontFamily: 'arial',
        ),
      ),
    );
  }
}