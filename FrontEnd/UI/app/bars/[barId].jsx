import React from 'react';
import { View, Text, Image, StyleSheet, Pressable } from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { barData } from '../../lib/barData';
import { FontAwesome5 } from '@expo/vector-icons'; // Icon library for back arrow

export default function BarDetailScreen() {
  // Get the dynamic route parameter `barId` from the URL
  const { barId } = useLocalSearchParams();

  // Router instance to allow navigation actions like "back"
  const router = useRouter();

  // Lookup bar info from your data using the barId
  const bar = barData[barId];

  // Show an error message if no bar matches the given barId
  if (!bar) {
    return (
      <View style={styles.centered}>
        <Text style={styles.notFound}>Bar not found.</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      {/* Banner at top with back button and title */}
      <View style={styles.banner}>
        {/* Pressable back button on left */}
        <Pressable
          onPress={() => router.back()} // Navigate back on press
          style={styles.backButton} // Styling for touch area
        >
          {/* Back arrow icon */}
          <FontAwesome5 name="arrow-left" size={24} color="#fff" />
        </Pressable>

        {/* Title text of the banner */}
        <Text style={styles.bannerTitle}>Bar Details</Text>
      </View>

      {/* Main content area */}
      {/* Bar name */}
      <Text style={styles.title}>{bar.name}</Text>

      {/* Bar image */}
      <Image source={bar.image} style={styles.image} />

      {/* Bar description text */}
      <Text style={styles.description}>{bar.description}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 24, // Outer padding for the whole page content
    paddingTop: 16, // Extra top padding to visually separate from banner
    backgroundColor: '#1c1c1e', // Background color of the page
    flex: 1, // Fill entire available screen space vertically
  },
  banner: {
    flexDirection: 'row', // Arrange back button and title horizontally
    alignItems: 'center', // Vertically center items in banner
    backgroundColor: '#111', // Dark background for banner
    paddingVertical: 12, // Vertical padding inside banner
    paddingHorizontal: 16, // Horizontal padding inside banner
    marginBottom: 16, // Space below banner before main content
    borderRadius: 8, // Rounded corners for banner
  },
  backButton: {
    marginRight: 16, // Space between back button and title text
    padding: 6, // Padding around icon to increase tap target size
  },
  bannerTitle: {
    fontSize: 20, // Font size of banner title text
    fontWeight: 'bold', // Make title text bold
    color: '#fff', // White color text for contrast on dark banner
  },
  title: {
    fontSize: 32, // Main bar name font size
    fontWeight: 'bold', // Bold font weight for bar name
    color: '#fff', // White text color for title
    marginBottom: 16, // Space below the title before image
  },
  image: {
    width: '100%', // Full width image
    height: 200, // Fixed height for image
    resizeMode: 'cover', // Scale image to cover area without distortion
    borderRadius: 12, // Rounded corners on image
    marginBottom: 20, // Space below image before description text
  },
  description: {
    fontSize: 18, // Font size of description text
    color: '#ccc', // Light gray text color for description
  },
  centered: {
    flex: 1, // Take full available space
    justifyContent: 'center', // Center content vertically
    alignItems: 'center', // Center content horizontally
    backgroundColor: '#1c1c1e', // Same background color as container
  },
  notFound: {
    fontSize: 20, // Font size for error message text
    color: '#ff3b30', // Bright red color to indicate error
  },
});
