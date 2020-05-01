import 'package:flutter/material.dart';
import 'package:edgevalue/localization/app_translations.dart';
import 'package:edgevalue/widgets/navigation_bar/navigation_bar_item_desktop.dart';

class NavigationBarDesktop extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 65,
      child: Padding(
        padding: const EdgeInsets.fromLTRB(0, 0, 50, 0),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.end,
          children: <Widget>[
            NavigationBarItemDesktop(title: Translations.of(context).text('contact_us_text')),
            SizedBox(width: 15),
            NavigationBarItemDesktop(title: Translations.of(context).text('about_us_text')),
          ],
        ),
      ),
    );
  }
}
