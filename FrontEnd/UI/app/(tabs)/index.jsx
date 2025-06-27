import React from 'react';
import { View, Text, StyleSheet, Button, Pressable } from 'react-native';
import { useRouter } from 'expo-router';
import { useSafeAreaInsets } from 'react-native-safe-area-context';

export default function Tab() {
  const router = useRouter();
  const insets = useSafeAreaInsets();
  
  return (
    <View style={styles.container}>
      <Pressable
        style={[
          styles.floatingButton,
          { top: insets.top + 20, left: insets.left + 10 }
        ]}
        onPress={() => router.push('/profile')}
      >
        <Text style={styles.buttonText}>Profile</Text>
      </Pressable>
      <Text>19 POUNDS OF STEAK</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#',
  },
  floatingButton: {
    position: 'absolute',
    top: 40, // Adjust for status bar if needed
    left: 20,
    backgroundColor: '#007AFF',
    paddingVertical: 8,
    paddingHorizontal: 16,
    borderRadius: 20,
    zIndex: 10,
  },
  buttonText: {
    color: 'white',
    fontWeight: 'bold',
  },
});
