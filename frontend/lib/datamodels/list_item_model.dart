import 'package:flutter/material.dart';

class ListItemModel extends StatefulWidget {
  ListItemModel({
    this.title = '',
    this.color = Colors.white,
    this.hoverColor = Colors.lightBlue,
  });

  final String title;
  final Color color, hoverColor;

  @override
  _ListItemModelState createState() => _ListItemModelState();
}

class _ListItemModelState extends State<ListItemModel> {
  Color _currentColor;

  void _updateCurrentColor(bool mouseHover) {
    setState(() {
      _currentColor = mouseHover ? widget.hoverColor : widget.color;
    });
  }

  @override
  void initState() {
    super.initState();
    _currentColor = widget.color;
  }

  @override
  Widget build(BuildContext context) {
    return MouseRegion(
      onEnter: (_) { _updateCurrentColor(true); },
      onExit: (_) { _updateCurrentColor(false); },
      child: Ink(
        color: _currentColor,
        child: ListTile(
          title: Text(widget.title),
        ),
      ),
    );
  }
}
