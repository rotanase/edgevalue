import 'package:flutter/material.dart';

class NavigationBarItemDesktop extends StatelessWidget {
  const NavigationBarItemDesktop({Key key, this.title}) : super(key: key);

  final String title;

  @override
  Widget build(BuildContext context) {
    return Text(
      title,
      style: TextStyle(fontSize: 14),
    );
  }
}
