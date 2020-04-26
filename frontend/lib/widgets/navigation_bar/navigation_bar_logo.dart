import 'package:flutter/material.dart';

class NavigationBarLogo extends StatelessWidget {
  const NavigationBarLogo({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 130,
      width: 200,
      child: Image.asset('assets/logo.png'),
    );
  }
}
