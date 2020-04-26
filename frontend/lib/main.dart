import 'package:flutter/material.dart';
import 'package:edgevalue/views/layout_template.dart';

void main() => runApp(EdgeValue());

class EdgeValue extends StatelessWidget {
  @override
  Widget build(BuildContext context) => MaterialApp(
    title: 'Edge Value',
    home: LayoutTemplate(),
  );
}
