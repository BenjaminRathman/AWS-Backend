import React from 'react';
import { View, Text, StyleSheet, Dimensions, FlatList } from 'react-native';

const DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

export default function SpecialsTab() {
  const screenWidth = Dimensions.get('window').width;

  return (
    <FlatList
      data={DAYS}
      horizontal
      pagingEnabled
      keyExtractor={(item, index) => index.toString()}
      showsHorizontalScrollIndicator={false}
      renderItem={({ item }) => (
        <View style={[styles.page, { width: screenWidth }]}>
          {/* Custom header for each day */}
          <View style={styles.header}>
            <Text style={styles.headerText}>{item}</Text>
          </View>

          {/* Unique content for each day */}
          <View style={styles.content}>
            <Text>Specials for {item}</Text>
          </View>
        </View>
      )}
    />
  );
}

const styles = StyleSheet.create({
  page: {
    flex: 1,
  },
  header: {
    backgroundColor: '#f2f2f2',
    paddingTop: 50,
    paddingBottom: 16,
    paddingHorizontal: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  headerText: {
    fontSize: 24,
    fontWeight: 'bold',
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});
