import 'package:flutter/material.dart';

class BetterListTile extends StatefulWidget {
  BetterListTile({
    this.title = '',
    this.subtitle = '',
    this.secondSubtitle = '',
    this.color = Colors.white,
    this.hoverColor = Colors.lightBlue,
  });

  final String title, subtitle, secondSubtitle;
  final Color color, hoverColor;

  @override
  _BetterListTileState createState() => _BetterListTileState();
}

class _BetterListTileState extends State<BetterListTile> {
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
          subtitle: Text(widget.subtitle + ' / ' + widget.secondSubtitle),
        ),
      ),
    );
  }
}
