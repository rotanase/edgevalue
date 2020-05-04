import 'package:flutter/material.dart';
import 'package:responsive_builder/responsive_builder.dart';

import 'search_bar_desktop.dart';

class SearchBar extends StatelessWidget {

  // Used for the text field widget of this search bar.
  final TextEditingController controller;

  SearchBar({this.controller});

  @override
  Widget build(BuildContext context) {
    return ScreenTypeLayout(
      // TODO: mobile navigation bar
      desktop: SearchBarDesktop(controller: controller),
    );
  }
}
