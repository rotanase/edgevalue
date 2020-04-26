import 'package:flutter/material.dart';

import 'navigation_bar_item_desktop.dart';
import 'navigation_bar_logo.dart';

class NavigationBarDesktop extends StatelessWidget {
  const NavigationBarDesktop({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 100,
      child: Row(
        children: <Widget>[
          NavigationBarLogo(),
          Row(
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              NavigationBarItemDesktop(title: 'Ceva 1'),
              SizedBox(width: 60),
              NavigationBarItemDesktop(title: 'Ceva 2'),
              SizedBox(width: 60),
              NavigationBarItemDesktop(title: 'Ceva 3'),
            ],
          ),
        ],
      ),
    );
  }
}
