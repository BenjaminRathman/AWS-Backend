import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Dimensions } from 'react-native';

const specialsByDay = {
    Sunday: [
        { name: 'Restaurant 1', specials: 'No specials today!' },
        { name: 'Restaurant 2', specials: 'No specials today!' },
        { name: 'Restaurant 3', specials: 'Half-price wings' },
        { name: 'Restaurant 4', specials: 'Free drink with entree' },
        { name: 'Restaurant 5', specials: '20% off desserts' },
      ],
      Monday: [
        { name: 'Restaurant 1', specials: 'No specials today!' },
        { name: 'Restaurant 2', specials: 'No specials today!' },
        { name: 'Restaurant 3', specials: 'Half-price burgers' },
        { name: 'Restaurant 4', specials: 'Buy 1 get 1 free pizza' },
        { name: 'Restaurant 5', specials: '20% off all desserts' },
      ],
      Tuesday: [
        { name: 'Restaurant 1', specials: 'Free salad with entree' },
        { name: 'Restaurant 2', specials: '$3 Tacos' },
        { name: 'Restaurant 3', specials: 'Half-price wings' },
        { name: 'Restaurant 4', specials: 'Free drink with entree' },
        { name: 'Restaurant 5', specials: '20% off desserts' },
      ],
      Wednesday: [
        { name: 'Restaurant 1', specials: 'No specials today!' },
        { name: 'Restaurant 2', specials: 'No specials today!' },
        { name: 'Restaurant 3', specials: 'Half-price burgers' },
        { name: 'Restaurant 4', specials: 'Buy 1 get 1 free pizza' },
        { name: 'Restaurant 5', specials: '20% off all desserts' },
      ],
      Thursday: [
        { name: 'Restaurant 1', specials: 'No specials today!' },
        { name: 'Restaurant 2', specials: 'No specials today!' },
        { name: 'Restaurant 3', specials: 'Half-price burgers' },
        { name: 'Restaurant 4', specials: 'Buy 1 get 1 free pizza' },
        { name: 'Restaurant 5', specials: '20% off all desserts' },
      ],
      Friday: [
        { name: 'Restaurant 1', specials: 'No specials today!' },
        { name: 'Restaurant 2', specials: 'No specials today!' },
        { name: 'Restaurant 3', specials: 'Half-price burgers' },
        { name: 'Restaurant 4', specials: 'Buy 1 get 1 free pizza' },
        { name: 'Restaurant 5', specials: '20% off all desserts' },
      ],
      Saturday: [
        { name: 'Restaurant 1', specials: 'No specials today!' },
        { name: 'Restaurant 2', specials: 'No specials today!' },
        { name: 'Restaurant 3', specials: 'Half-price burgers' },
        { name: 'Restaurant 4', specials: 'Buy 1 get 1 free pizza' },
        { name: 'Restaurant 5', specials: '20% off all desserts' },
      ],
    };

export default function SpecialsPage({ day }) {
  const screenWidth = Dimensions.get('window').width;

  const restaurantsData = specialsByDay[day] || [];

  // Initialize expandedIndexes with all indexes open by default
  const [expandedIndexes, setExpandedIndexes] = useState(
    restaurantsData.map((_, i) => i)
  );

  const toggleExpand = (index) => {
    if (expandedIndexes.includes(index)) {
      // If index is already open, remove it (close)
      setExpandedIndexes(expandedIndexes.filter(i => i !== index));
    } else {
      // If index is closed, add it (open)
      setExpandedIndexes([...expandedIndexes, index]);
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerText}>{day}</Text>
      </View>

      <ScrollView style={styles.content} showsVerticalScrollIndicator={false}>
        {restaurantsData.map((restaurant, index) => (
          <View key={index} style={styles.restaurantContainer}>
            <TouchableOpacity
              style={styles.tab}
              activeOpacity={0.7}
              onPress={() => toggleExpand(index)}
            >
              <Text style={styles.tabText}>{restaurant.name}</Text>
            </TouchableOpacity>

            {/* Check if this index is in expandedIndexes array */}
            {expandedIndexes.includes(index) && (
              <View style={styles.dropdownContent}>
                <Text style={styles.specialsText}>{restaurant.specials}</Text>
              </View>
            )}
          </View>
        ))}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { 
    flex: 1,
    backgroundColor: '#f0f0f0'
  },
  header: {
    backgroundColor: '#f6da0b',
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
    paddingVertical: 10,
  },
  restaurantContainer: {
    marginBottom: 10,
    paddingHorizontal: 0,
  },
  tab: {
    backgroundColor: '#595959', // color of each horizontal tab
    paddingVertical: 12,
    paddingHorizontal: 16,
    borderRadius: 6,
    width: '100%',
    alignSelf: 'stretch',
  },
  tabText: {
    fontSize: 18,
    fontWeight: '600',
    color: 'white',
    fontFamily: 'Roboto',
  },
  dropdownContent: {
    padding: 12,
    marginTop: 4,
    borderRadius: 6,
  },
  specialsText: {
    fontSize: 16,
    color: '#333',
  },
});
