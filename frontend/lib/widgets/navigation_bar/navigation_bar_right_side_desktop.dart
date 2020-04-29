import 'package:flutter/material.dart';
import 'package:edgevalue/localization/app_translations.dart';

import 'navigation_bar_item_desktop.dart';

class NavigationBarRightSide extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(0, 0, 50, 0),
      child: Row(
        children: <Widget>[
          NavigationBarItemDesktop(title: Translations.of(context).text('login')),
        ],
      ),
    );
  }
}
