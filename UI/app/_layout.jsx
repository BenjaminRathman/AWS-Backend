import { Stack, Tabs } from "expo-router";
import { Text } from "react-native";

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
    </Stack>
  );
}