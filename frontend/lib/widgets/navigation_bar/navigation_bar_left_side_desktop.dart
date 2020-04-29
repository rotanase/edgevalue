import 'package:flutter/material.dart';
import 'package:edgevalue/widgets/search_bar/search_bar.dart';
import 'navigation_bar_logo.dart';
import 'navigation_bar_item_desktop.dart';

class NavigationBarLeftSide extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Row(
      children: <Widget>[
        NavigationBarLogo(),
        NavigationBarItemDesktop(title: 'Ceva 1'),
        SizedBox(width: 15),
        NavigationBarItemDesktop(title: 'Ceva 2'),
        SizedBox(width: 15),
        NavigationBarItemDesktop(title: 'Ceva 3'),
        SizedBox(width: 15),
        SearchBar(),
      ],
    );
  }
}
