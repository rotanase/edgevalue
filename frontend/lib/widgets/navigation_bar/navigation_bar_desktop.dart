import 'package:flutter/material.dart';
import 'package:edgevalue/widgets/navigation_bar/navigation_bar_left_side_desktop.dart';
import 'package:edgevalue/widgets/navigation_bar/navigation_bar_right_side_desktop.dart';

class NavigationBarDesktop extends StatelessWidget {
  const NavigationBarDesktop({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 65,
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
