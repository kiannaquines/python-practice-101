 final List<Office> _listOfOffices = [];
  int? _selectedOfficeId;
  bool _officesCached = false;

  Future<List<Office>> fetchOffices() async {
    final response = await http.get(Uri.parse('$baseApiUrl/offices'));
    if (response.statusCode == 200) {
      final Map<String, dynamic> data = jsonDecode(response.body);
      final officeResponse = OfficeResponse.fromJson(data);
      return officeResponse.offices;
    } else {
      throw Exception('Failed to load offices');
    }
  }

  void onOfficeTextFieldTap() async {
    try {
      if (!_officesCached) {
        final fetchedOffices = await fetchOffices();
        setState(() {
          _listOfOffices.clear();
          _listOfOffices.addAll(fetchedOffices);
          _officesCached = true; // mark cache as populated
        });
      }

      DropDownState<String>(
        dropDown: DropDown<String>(
          isDismissible: true,
          enableMultipleSelection: false,
          bottomSheetTitle: const Text(
            'Select Office',
            style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20.0),
          ),
          dropDownBackgroundColor: Colors.white,
          submitButtonText: 'Save',
          clearButtonText: 'Clear',
          data:
              _listOfOffices
                  .map(
                    (office) => SelectedListItem<String>(data: office.office),
                  )
                  .toList(),
          onSelected: (selectedItems) {
            if (selectedItems.isNotEmpty) {
              final selectedOfficeName = selectedItems.first.data;
              final selectedOffice = _listOfOffices.firstWhere(
                (office) => office.office == selectedOfficeName,
              );

              setState(() {
                _officeController.text = selectedOffice.office;
                _selectedOfficeId = selectedOffice.id;
              });
            }
          },
        ),
      ).showModal(context);
    } catch (e) {
      debugPrint('Failed to load offices: $e');
      ScaffoldMessenger.of(
        context,
      ).showSnackBar(SnackBar(content: Text('Error fetching offices')));
    }
  }
