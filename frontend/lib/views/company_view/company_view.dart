import 'package:edgevalue/widgets/layout_template.dart';
import 'package:flutter/material.dart';

import 'navigation_bar.dart';

class CompanyView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return LayoutTemplate(
      navigationBar: NavigationBar(),
      body: Center(
        child: Text(
          'YUHUUU!',
          style: TextStyle(fontSize: 50),
        ),
      ),
    );
  }
}
