import 'package:flutter/material.dart';
import 'package:responsive_builder/responsive_builder.dart';
import 'package:edgevalue/widgets/centered_view.dart';

class LayoutTemplate extends StatelessWidget {
  final Widget navigationBar, body;

  LayoutTemplate({this.navigationBar, this.body});

  @override
  Widget build(BuildContext context) {
    return ResponsiveBuilder(
      builder: (context, platformInfo) => Scaffold(
        backgroundColor: Colors.white,
        body: CenteredView(
          child: Column(
            children: <Widget>[
              Flexible(
                flex: 1,
                child: navigationBar,
              ),
              Flexible(
                flex: 8,
                child: Scrollbar(
                  child: SingleChildScrollView(
                    child: body
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
