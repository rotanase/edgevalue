import 'package:flutter/material.dart';

class CenteredView extends StatefulWidget {
  final Widget child;
  const CenteredView({Key key, this.child}) : super(key: key);

  @override
  _CenteredViewState createState() => _CenteredViewState();
}

class _CenteredViewState extends State<CenteredView> {
  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.topCenter,
      child: ConstrainedBox(
        constraints: BoxConstraints(maxWidth: 2045),
        child: widget.child,
      ),
    );
  }
}
