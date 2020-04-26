import 'package:flutter/material.dart';
import 'package:responsive_builder/responsive_builder.dart';
import 'package:edgevalue/widgets/centered_view.dart';
import 'package:edgevalue/widgets/navigation_bar/navigation_bar.dart';

class LayoutTemplate extends StatelessWidget {
  const LayoutTemplate({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ResponsiveBuilder(
      builder: (context, platformInfo) => Scaffold(
        // TODO: mobile drawer
        backgroundColor: Colors.white,
        body: CenteredView(
          child: Column(
            children: <Widget>[
              NavigationBar(),
              Center(
                child: Text(
                  '12HOLA!!!',
                  style: TextStyle(fontSize: 50),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
