import 'package:flutter/material.dart';
import 'package:edgevalue/localization/app_translations.dart';
import 'package:edgevalue/widgets/navigation_bar/navigation_bar_item_desktop.dart';
import 'package:edgevalue/widgets/search_bar/search_bar_desktop.dart';
import 'package:edgevalue/viewmodels/search_bar_view_model.dart';

import 'navigation_bar_logo.dart';

class NavigationBarDesktop extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 65,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: <Widget>[
          Row(
            children: <Widget>[
              NavigationBarLogo(),
              NavigationBarItemDesktop(title: 'Ceva 1'),
              SizedBox(width: 15),
              NavigationBarItemDesktop(title: 'Ceva 2'),
              SizedBox(width: 15),
              NavigationBarItemDesktop(title: 'Ceva 3'),
              SizedBox(width: 15),
              SearchBarDesktop(
                hintText: Translations.of(context).text('search_bar_initial_text'),
                viewModel: SearchBarViewModel(), // TODO: save this controller for later use
              ),
            ],
          ),
          Padding(
            padding: const EdgeInsets.fromLTRB(0, 0, 50, 0),
            child: Row(
              children: <Widget>[
                NavigationBarItemDesktop(title: Translations.of(context).text('login')),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
