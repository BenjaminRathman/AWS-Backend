import { View, Text, StyleSheet } from 'react-native';


export default function Profile() {
  return (
    <View style={styles.container}>
      <Text>This is the profile page!</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
});