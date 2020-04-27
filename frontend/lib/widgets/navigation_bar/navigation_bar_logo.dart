import 'package:flutter/material.dart';

class NavigationBarLogo extends StatefulWidget {
  const NavigationBarLogo({Key key}) : super(key: key);

  @override
  _NavigationBarLogoState createState() => _NavigationBarLogoState();
}

class _NavigationBarLogoState extends State<NavigationBarLogo> {
  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 80,
      width: 150,
      child: Image.asset('assets/logo.png'),
    );
  }
}
