import 'package:flutter/material.dart';
import 'package:responsive_builder/responsive_builder.dart';
import 'package:edgevalue/widgets/search_bar/search_bar_desktop.dart';

class SearchBar extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ScreenTypeLayout(
      // TODO: mobile implementation
      desktop: SearchBarDesktop(),
    );
  }
}
