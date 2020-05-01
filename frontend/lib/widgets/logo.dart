import 'package:flutter/material.dart';

class Logo extends StatelessWidget {
  Logo({this.height, this.width});

  final double height, width;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: height,
      width: width,
      child: Image.asset('assets/logo.png'),
    );
  }
}
