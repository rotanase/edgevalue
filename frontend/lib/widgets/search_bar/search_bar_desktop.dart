import 'package:flutter/material.dart';
import 'package:edgevalue/viewmodels/search_bar_view_model.dart';

class SearchBarDesktop extends StatefulWidget {
  final String hintText;
  final double height, width, resultsOverlayWidth;
  final TextEditingController controller;

  // Default values are set for the navigation bar
  SearchBarDesktop({
    this.height = 30,
    this.width = 250,
    this.resultsOverlayWidth = 250 * 1.5,
    this.hintText = '',
    @required this.controller,
  });

  @override
  _SearchBarDesktopState createState() => _SearchBarDesktopState();
}

class _SearchBarDesktopState extends State<SearchBarDesktop> {
  TextEditingController get controller => widget.controller;
  
  // `ModelView` for this search bar.
  SearchBarViewModel _model = SearchBarViewModel();

  // An overlay in which search results are shown.
  OverlayEntry _resultsOverlayEntry;

  // Builder for the overlay entry which contains search results.
  OverlayEntry _createResultsOverlayEntry() {
    RenderBox rBox = context.findRenderObject();
    Offset rBoxOffset = rBox.localToGlobal(Offset.zero);
    Size rBoxSize = rBox.size;

    return OverlayEntry(
      builder: (context) => Positioned(
        left: rBoxOffset.dx,
        top: rBoxOffset.dy + rBoxSize.height + 5.0,
        width: widget.resultsOverlayWidth,
        child: MouseRegion(
          onEnter: (_) => _model.mouseHoveringResultsOverlayEntry = true,
          onExit: (_) => _model.mouseHoveringResultsOverlayEntry = false,
          child: GestureDetector(
            onTap: _model.onResultsOverlayEntryTap,
            child: Material(
              elevation: 4.0,
              child: _model.waitingForResults
              ? LinearProgressIndicator()
              : _model.searchResultsListView,
            ),
          ),
        ),
      ),
    );
  }

  // Always remove the `_resultsOverlayEntry` using this method.
  void _removeResultsOverlayEntry() {
    _resultsOverlayEntry?.remove();
    _resultsOverlayEntry = null;
  }
  
  /*
   * Creates / Updates the results overlay, or remove it
   * if there is no input string from the user.
   */
  void _updateResultsOverlayEntry() {
    if (controller.text.isNotEmpty) {
      if (_resultsOverlayEntry == null) {
        _resultsOverlayEntry = _createResultsOverlayEntry();
        Overlay.of(context).insert(_resultsOverlayEntry);
      } else {
        _resultsOverlayEntry.markNeedsBuild();
      }
    } else {
      _removeResultsOverlayEntry();
    }
  }

  @override
  void initState() {
    super.initState();
    _model.searchBarfocusNode.addListener(() {
      if (_model.searchBarfocusNode.hasFocus) {
        _updateResultsOverlayEntry();
      } else if (!_model.mouseHoveringResultsOverlayEntry) {
        _removeResultsOverlayEntry();
      }
    });
  }

  @override
  void dispose() {
    _removeResultsOverlayEntry();
    super.dispose();
  }

  // Helper method for `build()`.
  OutlineInputBorder _searchBarOutlineBorder() {
    return OutlineInputBorder(
      borderRadius: BorderRadius.circular(100),
      borderSide: BorderSide(
        color: Colors.grey[700],
        width: 0.5,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      height: widget.height,
      width: widget.width,
      child: RawKeyboardListener(
        focusNode: _model.keyboadListenerfocusNode,
        onKey: (event) => _model.onKey(controller.text, event),
        child: TextFormField(
          cursorColor: Colors.black,
          cursorWidth: 0.25,
          decoration: InputDecoration(
            contentPadding: EdgeInsets.zero,
            prefixIcon: Icon(
              Icons.search,
              color: Colors.grey[600],
            ),
            enabledBorder: _searchBarOutlineBorder(),
            focusedBorder: _searchBarOutlineBorder(),
            hintText: widget.hintText,
          ),
          onChanged: (inputText) {
            _updateResultsOverlayEntry();
            _model.getSearchResults(
              inputText,
              () => _resultsOverlayEntry?.markNeedsBuild(),
            );
          },
          onFieldSubmitted: _model.onFieldSubmitted,
          focusNode: _model.searchBarfocusNode,
          controller: controller,
        ),
      ),
    );
  }
}
