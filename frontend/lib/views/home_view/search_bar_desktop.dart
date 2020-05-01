import 'package:edgevalue/localization/app_translations.dart';
import 'package:flutter/material.dart';
import 'package:edgevalue/widgets/search_bar/search_bar_desktop.dart' as widgets;

class SearchBarDesktop extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return widgets.SearchBarDesktop(
      height: 50,
      width: 600,
      resultsOverlayWidth: 600,
      hintText: Translations.of(context).text('home_search_bar_initial_text'),
    );
  }
}
