import 'package:flutter/material.dart';
import 'package:edgevalue/widgets/navigation_bar/navigation_bar_left_side_desktop.dart';
import 'package:edgevalue/widgets/navigation_bar/navigation_bar_right_side_desktop.dart';

class NavigationBarDesktop extends StatefulWidget {
  const NavigationBarDesktop({Key key}) : super(key: key);

  @override
  _NavigationBarDesktopState createState() => _NavigationBarDesktopState();
}

class _NavigationBarDesktopState extends State<NavigationBarDesktop> {
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 80,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: <Widget>[
          NavigationBarLeftSide(),
          NavigationBarRightSide(),
        ],
      ),
    );
  }
}
