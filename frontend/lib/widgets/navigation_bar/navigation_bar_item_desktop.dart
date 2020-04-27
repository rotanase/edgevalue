import 'package:flutter/material.dart';

class NavigationBarItemDesktop extends StatefulWidget {
  const NavigationBarItemDesktop({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _NavigationBarItemDesktopState createState() => _NavigationBarItemDesktopState();
}

class _NavigationBarItemDesktopState extends State<NavigationBarItemDesktop> {
  @override
  Widget build(BuildContext context) {
    return Text(
      widget.title,
      style: TextStyle(fontSize: 14),
    );
  }
}
