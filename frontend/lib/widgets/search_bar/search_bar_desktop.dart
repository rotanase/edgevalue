import 'package:flutter/material.dart';
import 'package:edgevalue/localization/app_translations.dart';
import 'package:edgevalue/viewmodels/search_results_view_model.dart';

class SearchBarDesktop extends StatefulWidget {
  @override
  _SearchBarDesktopState createState() => _SearchBarDesktopState();
}

class _SearchBarDesktopState extends State<SearchBarDesktop> {

  // Used to hide `_resultsOverlay` when this search bar looses focus.
  final FocusNode _focusNode = FocusNode();

  // Used for the text field widget of this search bar.
  final TextEditingController _textEditingController = TextEditingController();

  // Used as the ViewModel for this search bar.
  final SearchResultsViewModel _resultsViewModel = SearchResultsViewModel();

  // An overlay in which search results are shown.
  OverlayEntry _resultsOverlayEntry;
  bool _waitingForResults = true;

  /*
   * Helper method to remove `_resultsOverlayEntry`.
   * Always set it to null if you delete it otherwise.
   */
  void _removeResultsOverlayEntry() {
    _resultsOverlayEntry?.remove();
    _resultsOverlayEntry = null;
  }

  /*
   * Helper method, it creates an overlay entry which contains
   * search results. Called by _showResultsOverlayEntry().
   */
  OverlayEntry _createResultsOverlayEntry() {
    RenderBox rBox = context.findRenderObject();
    Offset rBoxOffset = rBox.localToGlobal(Offset.zero);
    Size rBoxSize = rBox.size;

    return OverlayEntry(
      builder: (context) => Positioned(
        left: rBoxOffset.dx,
        top: rBoxOffset.dy + rBoxSize.height + 5.0,
        width: rBoxSize.width * 1.5,
        child: Material(
          elevation: 4.0,
          child: _waitingForResults ? LinearProgressIndicator() :
          (_resultsViewModel?.searchResults ?? LinearProgressIndicator()),
        ),
      ),
    );
  }

  /*
   * Creates / Updates the results overlay, or remove it
   * if there is no input string from the user.
   */
  void _showResultsOverlayEntry() {
    if (_textEditingController.text.isNotEmpty) {
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
    _focusNode.addListener(() {
      if (_focusNode.hasFocus) {
        _showResultsOverlayEntry();
      } else {
        _removeResultsOverlayEntry();
      }
    });
  }

  @override
  void dispose() {
    _removeResultsOverlayEntry();
    _textEditingController.dispose();
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
      height: 30,
      width: 250,
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
          hintText: Translations.of(context).text('search_bar_initial_text'),
        ),
        onChanged: (tickerToSearch) {
          _waitingForResults = true;
          _showResultsOverlayEntry();
          print ('Hello1');
          _resultsViewModel.getSearchResults(tickerToSearch, () {
            _waitingForResults = false;
            _resultsOverlayEntry?.markNeedsBuild();
          });
        },
        focusNode: _focusNode,
        controller: _textEditingController,
      ),
    );
  }
}
